---
id: UDG@20.15.2@MMLCommand@DSP OSPFORIGINATELSA
type: MMLCommand
name: DSP OSPFORIGINATELSA（查询Router LSA生成流程的信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFORIGINATELSA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询Router LSA生成流程的信息
status: active
---

# DSP OSPFORIGINATELSA（查询Router LSA生成流程的信息）

## 功能

该命令用于查询Router LSA生成流程的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [Router LSA生成流程的信息（OSPFORIGINATELSA）](configobject/UDG/20.15.2/OSPFORIGINATELSA.md)

## 使用实例

查询OSPF进程1的Router LSA生成流程的信息：

```
DSP OSPFORIGINATELSA:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
   OSPF进程号  =  1
       区域号  =  0.0.0.0
   路由器标识  =  10.10.10.1
Flush LSA计数  =  0
 创建失败计数  =  0
 添加失败计数  =  0
 查找失败计数  =  0
 接收相同计数  =  0
  抑制LSA计数  =  0
(Number of results = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Router-LSA生成流程的信息（DSP-OSPFORIGINATELSA）_49961438.md`
