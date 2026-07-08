---
id: UDG@20.15.2@MMLCommand@LST BANDWIDTHMNG
type: MMLCommand
name: LST BANDWIDTHMNG（查询带宽管理参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BANDWIDTHMNG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理参数
status: active
---

# LST BANDWIDTHMNG（查询带宽管理参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询带宽控制器中用户组级业务带宽和连接数配置的生效范围，以及带宽资源动态统计和调整周期。

## 注意事项

如果没有配置过生效范围和周期参数，则显示默认值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/BANDWIDTHMNG]] · 带宽管理参数（BANDWIDTHMNG）

## 使用实例

假如运营商希望查询带宽和连接数生效范围，及资源统计周期：

```
LST BANDWIDTHMNG:;
```

```

RETCODE = 0  操作成功。

带宽管理参数信息
----------------
                    带宽管理生效范围  =  CPU Level
                      统计周期（秒）  =  5
承诺信息速率最低保护值（千比特每秒）  =  0
峰值信息速率最低保护值（千比特每秒）  =  0
               用户级业务带宽控制选项 = PCC Rule 不关注
                             调整系数 = 10
        基于Shaping的组级带宽控制开关 = 不使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询带宽管理参数（LST-BANDWIDTHMNG）_86526893.md`
