---
id: UDG@20.15.2@MMLCommand@DSP FEISWHEALTHSTATE
type: MMLCommand
name: DSP FEISWHEALTHSTATE（显示FEISW健康状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FEISWHEALTHSTATE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- FEISW健康状态信息
status: active
---

# DSP FEISWHEALTHSTATE（显示FEISW健康状态）

## 功能

该命令用于查看FEISW健康状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/FEISWHEALTHSTATE]] · FEISW健康状态（FEISWHEALTHSTATE）

## 使用实例

查询FEISW健康状态：

```
DSP FEISWHEALTHSTATE:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                           组件PID  =  9175063
                           组件CID  =  2156658717
                          组件句柄  =  2405659432
                          输入个数  =  50
                          输入大小  =  72
                          最大实例  =  4
                        最大调度值  =  100
                          跟踪大小  =  0
                          事件类型  =  0
                            发送ID  =  0
                          平滑状态  =  Normal
                      转发引擎个数  =  0
             初始化第一阶段完成时间  =  2016-10-03 00:20:30.471
             初始化第二阶段完成时间  =  2016-10-03 00:20:30.491
             初始化第三阶段完成时间  =  2016-10-03 00:20:31.511
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示FEISW健康状态（DSP-FEISWHEALTHSTATE）_00601249.md`
