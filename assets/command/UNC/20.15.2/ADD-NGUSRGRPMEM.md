---
id: UNC@20.15.2@MMLCommand@ADD NGUSRGRPMEM
type: MMLCommand
name: ADD NGUSRGRPMEM（增加5G用户群成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGUSRGRPMEM
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- 用户群组成员管理
status: active
---

# ADD NGUSRGRPMEM（增加5G用户群成员）

## 功能

**适用NF：AMF**

该命令用于为5G用户群增加一条用户群成员记录。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入10000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRGRPID | 用户群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G用户群标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数表示用户群的描述信息，在运维中起助记作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGUSRGRPMEM]] · 5G用户群成员（NGUSRGRPMEM）

## 使用实例

增加一条用户群成员记录，用户群标识为20，IMSI前缀为123456，描述信息为“SomeTown”，执行如下命令：

```
ADD NGUSRGRPMEM: USRGRPID=20, IMSIPRE="123456", DESC="SomeTown";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NGUSRGRPMEM.md`
