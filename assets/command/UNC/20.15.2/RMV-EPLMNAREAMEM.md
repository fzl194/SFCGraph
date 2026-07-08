---
id: UNC@20.15.2@MMLCommand@RMV EPLMNAREAMEM
type: MMLCommand
name: RMV EPLMNAREAMEM（删除跟踪区域组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EPLMNAREAMEM
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 接入管理
- 等价PLMN区域管理
status: active
---

# RMV EPLMNAREAMEM（删除跟踪区域组成员）

## 功能

**适用NF：AMF**

该命令用于删除等价PLMN的跟踪区域组成员。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGRPID | 跟踪区域组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于标识使用相同等价PLMN策略的跟踪区域范围。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：无 |
| BGNTAC | 跟踪区域码起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于表示跟踪区编码的起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@EPLMNAREAMEM]] · 跟踪区域组成员（EPLMNAREAMEM）

## 使用实例

删除跟踪区域组标识为20，跟踪区编码起始值为120101，执行如下命令：

```
RMV EPLMNAREAMEM: TACGRPID=20, BGNTAC="120101";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-EPLMNAREAMEM.md`
