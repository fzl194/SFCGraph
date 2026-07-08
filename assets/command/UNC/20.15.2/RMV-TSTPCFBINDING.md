---
id: UNC@20.15.2@MMLCommand@RMV TSTPCFBINDING
type: MMLCommand
name: RMV TSTPCFBINDING（删除拨测用户和PCF的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TSTPCFBINDING
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- PCF拨测管理
status: active
---

# RMV TSTPCFBINDING（删除拨测用户和PCF的绑定关系）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于删除用户和PCF的绑定关系。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 支持分别以APN、IMSI、PCFINSTANCEID以及其组合作为查询条件删除已有配置。
- 不输入任何参数默认删除所有配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：本参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数来源于ADD APN中的“APN名称”参数， 需要符合APN命名规则。 |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：本参数用于指定用户IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是6~15。每个字符只能是十进制数字。<br>默认值：无<br>配置原则：<br>该参数不支持号段前缀匹配。 |
| PCFINSTANCEID | PCF实例标识 | 可选必选说明：可选参数<br>参数含义：本参数用于指定PCF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，大小写敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TSTPCFBINDING]] · 拨测用户和PCF的绑定关系（TSTPCFBINDING）

## 使用实例

- 删除IMSI是"123456789012345"，APN是"testAPn"的用户激活到PCFINSTANCEID是“testPcfInstanceId”的PCF的配置。
  ```
  RMV TSTPCFBINDING:APN="testAPN",IMSI="123456789012345",PCFINSTANCEID="testPcfInstanceId";
  ```
- 删除所有配置。
  ```
  RMV TSTPCFBINDING:;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-TSTPCFBINDING.md`
