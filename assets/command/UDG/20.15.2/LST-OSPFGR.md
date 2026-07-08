---
id: UDG@20.15.2@MMLCommand@LST OSPFGR
type: MMLCommand
name: LST OSPFGR（查询OSPF的平滑重启配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFGR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF的平滑重启配置
status: active
---

# LST OSPFGR（查询OSPF的平滑重启配置）

## 功能

该命令用于查询OSPF的平滑重启配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| HELPERROLEFLAG | 使能Helper模式 | 可选必选说明：可选参数<br>参数含义：使能Helper模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| HELPERFLAG | 使能GR | 可选必选说明：可选参数<br>参数含义：使能GR。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFGR]] · OSPF的平滑重启配置（OSPFGR）

## 使用实例

查询OSPF的平滑重启配置：

```
LST OSPFGR:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                     进程号  =  1
               只支持计划GR  =  FALSE
             使能Helper模式  =  TRUE
不检查Type-5和Type-7类的LSA  =  FALSE
           不支持Helper模式  =  FALSE
                     使能GR  =  TRUE
               Helper过滤值  =  NULL
             Helper过滤类型  =  空
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-OSPFGR.md`
