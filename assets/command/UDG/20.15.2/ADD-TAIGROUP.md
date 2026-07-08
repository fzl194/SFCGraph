---
id: UDG@20.15.2@MMLCommand@ADD TAIGROUP
type: MMLCommand
name: ADD TAIGROUP（添加一个新的TAI组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: TAIGROUP
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 3000
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- TAI组
status: active
---

# ADD TAIGROUP（添加一个新的TAI组）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来添加一个用于性能统计的TAI组，当需要使用基于TAI组维度进行性能统计时，使用此命令。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为3000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIGROUPNAME | 指定TAI组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAI组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，为3位数字，000～999。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网络号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网络号。<br>数据来源：全网规划<br>取值范围：字符串类型，可为2或3位数字，00~99或000~999。<br>默认值：无<br>配置原则：无 |
| TACTYPE | TAC 类型 | 可选必选说明：可选参数<br>参数含义：指定TAC类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- S1TAC：S1TAC。<br>- N2TAC：N2TAC。<br>默认值：S1TAC<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TAIGROUP]] · 指定的TAI组（TAIGROUP）

## 使用实例

假设运营商需要去添加一个新的TAI组beijing，mcc数值为123，mnc数值为456：

```
ADD TAIGROUP: TAIGROUPNAME="beijing", MCC="123", MNC="456";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-TAIGROUP.md`
