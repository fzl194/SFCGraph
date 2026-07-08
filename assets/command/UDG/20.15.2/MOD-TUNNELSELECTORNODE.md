---
id: UDG@20.15.2@MMLCommand@MOD TUNNELSELECTORNODE
type: MMLCommand
name: MOD TUNNELSELECTORNODE（修改隧道选择器节点）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: TUNNELSELECTORNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 隧道选择器管理
- 隧道选择器节点
status: active
---

# MOD TUNNELSELECTORNODE（修改隧道选择器节点）

## 功能

该命令用于修改隧道选择器节点。

## 注意事项

- 该命令执行后立即生效。
- 配置该命令前，必须已经配置了该节点指定隧道选择器的名字，必须配置了要修改的节点。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODESEQUENCE | 隧道选择器节点 | 可选必选说明：必选参数<br>参数含义：该参数用来指定隧道选择器节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| TNLSELECTORNAME | 隧道选择器名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定隧道选择器名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～40。<br>默认值：无 |
| MATCHMODE | 匹配模式 | 可选必选说明：必选参数<br>参数含义：该参数用来指定隧道选择器的匹配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TUNNELSELECTORNODE]] · 隧道选择器节点（TUNNELSELECTORNODE）

## 使用实例

修改隧道选择器a的一个节点属性，节点号为10：

```
MOD TUNNELSELECTORNODE:TNLSELECTORNAME="a",NODESEQUENCE=10,MATCHMODE=deny;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改隧道选择器节点（MOD-TUNNELSELECTORNODE）_49961954.md`
