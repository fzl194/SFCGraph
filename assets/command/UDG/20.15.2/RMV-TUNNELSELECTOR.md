---
id: UDG@20.15.2@MMLCommand@RMV TUNNELSELECTOR
type: MMLCommand
name: RMV TUNNELSELECTOR（删除隧道选择器）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TUNNELSELECTOR
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 隧道选择器管理
- 隧道选择器
status: active
---

# RMV TUNNELSELECTOR（删除隧道选择器）

## 功能

该命令用于删除隧道选择器。

## 注意事项

- 该命令执行后立即生效。
- 删除该隧道选择器时，要保证该隧道选择器被添加过。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNLSELECTORNAME | 隧道选择器名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定隧道选择器名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～40。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TUNNELSELECTOR]] · 隧道选择器（TUNNELSELECTOR）

## 使用实例

删除名称为a的隧道选择器：

```
RMV TUNNELSELECTOR:TNLSELECTORNAME="a";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-TUNNELSELECTOR.md`
