---
id: UDG@20.15.2@MMLCommand@LST OSPFDNBITSET
type: MMLCommand
name: LST OSPFDNBITSET（查询DN比特位配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFDNBITSET
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF DN比特位配置
status: active
---

# LST OSPFDNBITSET（查询DN比特位配置）

## 功能

该命令用于查询DN比特位配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFDNBITSET]] · DN比特位配置（OSPFDNBITSET）

## 使用实例

查询DN比特位配置：

```
LST OSPFDNBITSET:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                   进程号  =  1
    禁止配置ASE LSA的DN位  =  TRUE
   禁止配置NSSA LSA的DN位  =  FALSE
禁止配置Summary LSA的DN位  =  FALSE
    禁止检查ASE LSA的DN位  =  FALSE
   禁止检查NSSA LSA的DN位  =  FALSE
禁止检查Summary LSA的DN位  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-OSPFDNBITSET.md`
