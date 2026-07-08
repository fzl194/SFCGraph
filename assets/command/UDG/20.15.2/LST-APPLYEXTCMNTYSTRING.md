---
id: UDG@20.15.2@MMLCommand@LST APPLYEXTCMNTYSTRING
type: MMLCommand
name: LST APPLYEXTCMNTYSTRING（查询扩展团体属性值设置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APPLYEXTCMNTYSTRING
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 应用扩展团体属性值
status: active
---

# LST APPLYEXTCMNTYSTRING（查询扩展团体属性值设置）

## 功能

该命令用于列出应用扩展团体属性值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [扩展团体属性值设置（APPLYEXTCMNTYSTRING）](configobject/UDG/20.15.2/APPLYEXTCMNTYSTRING.md)

## 使用实例

查询设置扩展团体属性的操作值：

```
LST APPLYEXTCMNTYSTRING:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
      路由策略名字  =  a
    路由策略节点ID  =  10
扩展团体属性字符串  =  1:1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询扩展团体属性值设置（LST-APPLYEXTCMNTYSTRING）_00600973.md`
