---
id: UNC@20.15.2@MMLCommand@RMV UPIPDOMAIN
type: MMLCommand
name: RMV UPIPDOMAIN（删除当前UPF绑定的IP域）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UPIPDOMAIN
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UPF IP Domain管理
status: active
---

# RMV UPIPDOMAIN（删除当前UPF绑定的IP域）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除当前UPF绑定的IPDomain。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPNODE | UPF节点标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示UPF节点标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| IPDOMAIN | IP地址段归属的域 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IP地址段归属的域。例如当两个UPF上的IP地址段中存在重叠的地址时，可以配置地址段1归属IPDOAMAIN1，地址段2归属IPDOMAIN2，随UE IP将IPDOMAIN携带给PCF，PCF检测到IP地址冲突，不影响用户正常使用业务。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>SMF为每个IP地址段归属的域提供不同的标识符（如SMF NF实例标识符）。 |
| DNNSWITCH | DNN开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示是否打开指定DNN绑定UPNODE和IPDOMAIN的开关。<br>数据来源：全网规划<br>取值范围：<br>- “ENABLE（使能）”：Dnn配置使能<br>- “DISABLE（不使能）”：DNN配置不使能<br>默认值：无<br>配置原则：<br>若配置UPNODE和IPDomain之间的绑定关系，对所有DNN都生效，此参数应配置为DISABLE。<br>若配置UPNODE和IPDomain之间的绑定关系，只对某些DNN都生效，此参数应配置为ENABLE。 |
| DNN | 数据网络名称 | 可选必选说明：该参数在"DNNSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于表示数据网络名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [当前UPF绑定的IP域（UPIPDOMAIN）](configobject/UNC/20.15.2/UPIPDOMAIN.md)

## 使用实例

删除UPNODE为"upf_instance_1"的UPF与IPDomain的绑定关系

```
RMV UPIPDOMAIN: UPNODE="upf_instance_1", DNNSWITCH=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除当前UPF绑定的IP域（RMV-UPIPDOMAIN）_09652498.md`
