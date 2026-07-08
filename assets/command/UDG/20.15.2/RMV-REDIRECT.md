---
id: UDG@20.15.2@MMLCommand@RMV REDIRECT
type: MMLCommand
name: RMV REDIRECT（删除重定向）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: REDIRECT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- URL重定向控制
- 重定向
status: active
---

# RMV REDIRECT（删除重定向）

## 功能

**适用NF：PGW-U、UPF**

此命令用于运营商删除已经配置的URL重定向策略。

## 注意事项

- 该命令执行后立即生效。
- 输入REDIRECTNAME删除指定记录，不输入REDIRECTNAME删除所有记录。
- 如果Redirect配置已经被绑定到PccActionProp、ExtendPolicy、AdcPara、ContCateGBind、CfPfSpecAction或者CfTemplate则不允许删除，需先解除绑定，才能删除。
- 删除Redirect时，如果有业务正在使用该重定向目标，则可能会导致业务中断，或业务处理是非预期的。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REDIRECTNAME | 重定向名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置重定向配置名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [重定向（REDIRECT）](configobject/UDG/20.15.2/REDIRECT.md)

## 使用实例

运营商希望删除名为testredirect的URL重定向策略：

```
RMV REDIRECT:REDIRECTNAME="testredirect";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除重定向（RMV-REDIRECT）_82837530.md`
