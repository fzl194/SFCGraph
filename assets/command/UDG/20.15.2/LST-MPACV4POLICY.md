---
id: UDG@20.15.2@MMLCommand@LST MPACV4POLICY
type: MMLCommand
name: LST MPACV4POLICY（查询IPv4 MPAC策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MPACV4POLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- 管理平面接入控制IPv4策略
status: active
---

# LST MPACV4POLICY（查询IPv4 MPAC策略）

## 功能

该命令用于查询当前策略的基本配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定创建策略的策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MPACV4POLICY]] · IPv4 MPAC策略（MPACV4POLICY）

## 使用实例

查询当前策略的基本配置信息：

```
LST MPACV4POLICY:;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
          策略名称  =  policyV4
          描述信息  =  a test desc
        规则间步长  =  5
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPv4-MPAC策略（LST-MPACV4POLICY）_00841365.md`
