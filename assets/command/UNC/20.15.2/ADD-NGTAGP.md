---
id: UNC@20.15.2@MMLCommand@ADD NGTAGP
type: MMLCommand
name: ADD NGTAGP（增加5G TA群组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGTAGP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGRAN跟踪区管理
- NGRAN跟踪区群组管理
status: active
---

# ADD NGTAGP（增加5G TA群组）

## 功能

**适用NF：AMF**

该命令用于增加跟踪区群组记录。跟踪区群组用于定义一组TA组成的区域，以该区域为粒度进行业务策略控制。需要结合ADD NGTAGPMEM命令为跟踪区群组添加成员。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入256条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTAGPID | 跟踪区群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区群组标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~256。<br>默认值：无<br>配置原则：无 |
| DESC | 跟踪区群组描述 | 可选必选说明：可选参数<br>参数含义：该参数用于填写跟踪区群组的描述信息，例如群组名称等。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGTAGP]] · 5G TA群组（NGTAGP）

## 使用实例

增加一个TA群组，跟踪区群组标识为1，其群组描述为“shanghai”。

```
ADD NGTAGP: NGTAGPID=1, DESC="shanghai";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NGTAGP.md`
