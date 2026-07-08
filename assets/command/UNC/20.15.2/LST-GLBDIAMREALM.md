---
id: UNC@20.15.2@MMLCommand@LST GLBDIAMREALM
type: MMLCommand
name: LST GLBDIAMREALM（查询全局Diameter域）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBDIAMREALM
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter Realm
- 全局Realm
status: active
---

# LST GLBDIAMREALM（查询全局Diameter域）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询已配置的全局Diameter域与IMSI/MSISDN号段和应用类型的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATION | Diameter应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定全局Diameter域所属的Diameter应用。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- GY：Gy接口应用。<br>- GX：Gx接口应用。<br>- S6B：S6b接口应用。<br>默认值：无<br>配置原则：根据实际需要查询的应用类型选择对应的应用参数。 |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要与Diameter域绑定的IMSI/MSISDN号段的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [全局Diameter域（GLBDIAMREALM）](configobject/UNC/20.15.2/GLBDIAMREALM.md)

## 使用实例

- 查询全局Diameter域与Gx应用的绑定关系：
  ```
  LST GLBDIAMREALM: APPLICATION=GX;
  ```
  ```

  RETCODE = 0  操作成功

  全局Diameter域名
  ----------------
                    Diameter应用  =  Gx
             IMSI/MSISDN号段名称  =  imsi_msisdn_segment_1
                          优先级  =  101
     根据IMSI构造归属地Realm开关  =  不使能
                    Diameter域名  =  pcrf.huawei.com
  Supported-Features动态协商开关  =  不使能
   Supported-Feature AVP携带开关  =  使能
                     Feature列表  =  3GPP Rel-8 Gx功能&3GPP Rel-9 Gx功能
  (结果个数 = 1)

  ---    END
  ```
- 查询所有全局Diameter域的绑定关系：
  ```
  LST GLBDIAMREALM:;
  ```
  ```

  RETCODE = 0  操作成功

  全局Diameter域名
  ----------------
                    Diameter应用  =  Gx
             IMSI/MSISDN号段名称  =  imsi_msisdn_segment_1
                          优先级  =  101
     根据IMSI构造归属地Realm开关  =  不使能
                    Diameter域名  =  pcrf.huawei.com
  Supported-Features动态协商开关  =  不使能
   Supported-Feature AVP携带开关  =  使能
                     Feature列表  =  3GPP Rel-8 Gx功能&3GPP Rel-9 Gx功能
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局Diameter域（LST-GLBDIAMREALM）_09897283.md`
