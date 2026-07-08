---
id: UNC@20.15.2@MMLCommand@RMV TUNNELSELECTORNODE
type: MMLCommand
name: RMV TUNNELSELECTORNODE（删除隧道选择器节点）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV TUNNELSELECTORNODE（删除隧道选择器节点）

## 功能

该命令用于删除隧道选择器节点。

## 注意事项

- 该命令执行后立即生效。
- 配置该命令前，必须已经配置了该节点指定隧道选择器的名字和节点。
- 若删除节点，则当前节点下的条件语句与动作语句将被同时删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODESEQUENCE | 隧道选择器节点 | 可选必选说明：必选参数<br>参数含义：该参数用来指定隧道选择器节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| TNLSELECTORNAME | 隧道选择器名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定隧道选择器名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～40。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TUNNELSELECTORNODE]] · 隧道选择器节点（TUNNELSELECTORNODE）

## 使用实例

删除隧道选择器a的一个节点，节点号为10：

```
RMV TUNNELSELECTORNODE:TNLSELECTORNAME="a",NODESEQUENCE=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-TUNNELSELECTORNODE.md`
