---
id: UNC@20.15.2@MMLCommand@LST TUNNELSELECTORNODE
type: MMLCommand
name: LST TUNNELSELECTORNODE（查询隧道选择器节点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TUNNELSELECTORNODE
command_category: 查询类
effect_mode: ''
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

# LST TUNNELSELECTORNODE（查询隧道选择器节点）

## 功能

该命令用于查询隧道选择器节点。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNLSELECTORNAME | 隧道选择器名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定隧道选择器名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～40。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TUNNELSELECTORNODE]] · 隧道选择器节点（TUNNELSELECTORNODE）

## 使用实例

查询隧道选择器节点信息：

```
LST TUNNELSELECTORNODE:TNLSELECTORNAME="a";
```

```

RETCODE = 0  操作成功
结果如下
-------------------------
隧道选择器节点  =  6
隧道选择器名字  =  a
      匹配模式  =  允许
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TUNNELSELECTORNODE.md`
