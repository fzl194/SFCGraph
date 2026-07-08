---
id: UNC@20.15.2@MMLCommand@LST SQOSURPF
type: MMLCommand
name: LST SQOSURPF（查询流行为安全URPF）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SQOSURPF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 流行为安全URPF
status: active
---

# LST SQOSURPF（查询流行为安全URPF）

## 功能

该命令用来查询流行为下的URPF（单播反向路由转发）配置。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 流行为名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流行为名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [流行为安全URPF（SQOSURPF）](configobject/UNC/20.15.2/SQOSURPF.md)

## 使用实例

查询流行为下的安全URPF：

```
LST SQOSURPF:;
```

```
RETCODE = 0  操作成功

结果如下
------------------------
  流行为名称  =  b1
URPF检查类型  =  松散检查
匹配默认路由  =  接受
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询流行为安全URPF（LST-SQOSURPF）_00841749.md`
