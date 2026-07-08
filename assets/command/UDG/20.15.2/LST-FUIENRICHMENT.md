---
id: UDG@20.15.2@MMLCommand@LST FUIENRICHMENT
type: MMLCommand
name: LST FUIENRICHMENT（查询FUI增强参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FUIENRICHMENT
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- FUI重定向控制
- FUI增强
status: active
---

# LST FUIENRICHMENT（查询FUI增强参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示FUI增强参数，包括重定向携带信息名称等。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [FUI增强参数（FUIENRICHMENT）](configobject/UDG/20.15.2/FUIENRICHMENT.md)

## 使用实例

假如运营商想要查询FUIENRICHMENT的配置，检查重定向报文中携带了哪些信息，命令如下：

```
LST FUIENRICHMENT:;
```

```

RETCODE = 0  操作成功。

FUI增强参数信息
---------------
                      流控标识  =  不使能
            流控时间间隔（秒）  =  5
              端口识别功能开关  =  不使能
      欠费用户快速识别功能开关  =  使能
 FUI重定向加速功能使用的端口 1  =  53
 FUI重定向加速功能使用的端口 2  =  80
 FUI重定向加速功能使用的端口 3  =  8080
 FUI重定向加速功能使用的端口 4  =  9200
 FUI重定向加速功能使用的端口 5  =  9201
 FUI重定向加速功能使用的端口 6  =  0
 FUI重定向加速功能使用的端口 7  =  0
 FUI重定向加速功能使用的端口 8  =  0
 FUI重定向加速功能使用的端口 9  =  0
FUI重定向加速功能使用的端口 10  =  0
             重定向携带信息名称 = test
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询FUI增强参数（LST-FUIENRICHMENT）_86528461.md`
