---
id: UNC@20.15.2@MMLCommand@MOD TSTPCFBINDING
type: MMLCommand
name: MOD TSTPCFBINDING（修改拨测用户和PCF的绑定关系）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD TSTPCFBINDING（修改拨测用户和PCF的绑定关系）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于修改拨测用户和PCF的绑定关系，该命令执行后，如果用户未激活，用户激活后会选择该绑定的PCF，如果用户已激活，则继续使用原PCF，如果想要选择该绑定的PCF，需要将该用户去激活以后重新激活。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 拨测PCF完成后，要删除该配置。
- 不支持failover功能，若绑定的PCF故障，则用户激活失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数来源于ADD APN中的“APN名称”参数， 需要符合APN命名规则。 |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：本参数用于指定用户IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是6~15。每个字符只能是十进制数字。<br>默认值：无<br>配置原则：<br>该参数不支持号段前缀匹配。 |
| PCFINSTANCEID | PCF实例标识 | 可选必选说明：可选参数<br>参数含义：本参数用于指定PCF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，大小写敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [拨测用户和PCF的绑定关系（TSTPCFBINDING）](configobject/UNC/20.15.2/TSTPCFBINDING.md)

## 使用实例

修改IMSI是"123456789012345"，APN是"testAPn"的用户激活到PCFINSTANCEID是“testPcfInstanceId2”的PCF。

```
MOD TSTPCFBINDING:APN="testAPN",IMSI="123456789012345",PCFINSTANCEID="testPcfInstanceId2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改拨测用户和PCF的绑定关系（MOD-TSTPCFBINDING）_22836793.md`
