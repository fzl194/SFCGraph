---
id: UNC@20.15.2@MMLCommand@LST UPIPDOMAIN
type: MMLCommand
name: LST UPIPDOMAIN（查询当前UPF绑定的IP域）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPIPDOMAIN
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UPF IP Domain管理
status: active
---

# LST UPIPDOMAIN（查询当前UPF绑定的IP域）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查看当前UPF绑定的IPDOMAIN。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPNODE | UPF节点标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示UPF节点标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| DNNSWITCH | DNN开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否打开指定DNN绑定UPNODE和IPDOMAIN的开关。<br>数据来源：全网规划<br>取值范围：<br>- “ENABLE（使能）”：Dnn配置使能<br>- “DISABLE（不使能）”：DNN配置不使能<br>默认值：无<br>配置原则：<br>若配置UPNODE和IPDomain之间的绑定关系，对所有DNN都生效，此参数应配置为DISABLE。<br>若配置UPNODE和IPDomain之间的绑定关系，只对某些DNN生效，此参数应配置为ENABLE。 |
| DNN | 数据网络名称 | 可选必选说明：该参数在"DNNSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于表示数据网络名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [当前UPF绑定的IP域（UPIPDOMAIN）](configobject/UNC/20.15.2/UPIPDOMAIN.md)

## 使用实例

- 查询所有UPF绑定的IPDOMAIN。
  ```
  %%LST UPIPDOMAIN:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  UPF节点标识    数据网络名称   IP地址段归属的域   DNN开关

  upf_instance_1  NULL             Domain_0         未使能
  upf_instance_1  huawei.com       Domain_1         使能
  (结果个数 = 2)

   -----    END
  ```
- 查询指定UpNode的UPF绑定的IPDOMAIN。
  ```
  %%LST UPIPDOMAIN: UPNODE="upf_instance_1", DNNSWITCH=DISABLE;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
       UPF节点标识  =  upf_instance_1
      数据网络名称  =  NULL
  IP地址段归属的域  =  Domain_0
            DNN开关 = 未使能
  (结果个数 = 1)

   -----    END
  ```
- 查询指定UpNode的UPF在指定DNN条件下绑定的IPDOMAIN。
  ```
  %%LST UPIPDOMAIN: UPNODE="upf_instance_1", DNNSWITCH=ENABLE, DNN="huawei.com";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
       UPF节点标识  =  upf_instance_1
      数据网络名称  =  huawei.com
  IP地址段归属的域  =  Domain_1
            DNN开关 = 使能
  (结果个数 = 1)

   -----    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询当前UPF绑定的IP域（LST-UPIPDOMAIN）_09651493.md`
