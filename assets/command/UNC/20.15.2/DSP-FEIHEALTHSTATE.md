---
id: UNC@20.15.2@MMLCommand@DSP FEIHEALTHSTATE
type: MMLCommand
name: DSP FEIHEALTHSTATE（显示FEI健康状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: FEIHEALTHSTATE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- FEI健康状态信息
status: active
---

# DSP FEIHEALTHSTATE（显示FEI健康状态）

## 功能

该命令用于查看FEI健康状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [FEI健康状态（FEIHEALTHSTATE）](configobject/UNC/20.15.2/FEIHEALTHSTATE.md)

## 使用实例

查询FEI健康状态：

```
DSP FEIHEALTHSTATE: RUNAME="VNODE_VNRS_VNFC_IPU_0065";
```

```
RETCODE = 0  操作成功。

结果如下
--------
                       组件PID  =  8323091
                       组件CID  =  2155806739
                     NHP表条目  =  262144
             NHP表内存（字节）  =  4194304
                     NST表条目  =  262144
             NST表内存（字节）  =  0
        通用路由封装隧道表条目  =  4096
通用路由封装隧道表内存（字节）  =  65536
                        HA状态  =  HA状态机为单主控，开工之后但是备上线之前
                 VNRS_VNFC类型  =  Ordinary
                          节点  =  4390657
            需要打开端口的数量  =  0
                      平滑使能  =  True
                   FES服务状态  =  Available
                   FES平滑状态  =  Done
                      平滑状态  =  Normal
                      输入个数  =  50
                      输入大小  =  72
                      最大实例  =  4
                    最大调度值  =  100
                      跟踪大小  =  0
                      事件类型  =  0
                        发送ID  =  0
                      节能开关  =  On
                休眠时间（us）  =  1
                      休眠阈值  =  1
                    检测窗口值  =  30
                  队列检测深度  =  32768
        初始化第一阶段完成时间  =  2017-12-19 13:57:52.553
        初始化第二阶段完成时间  =  2017-12-19 13:57:52.553
        初始化第三阶段完成时间  =  2017-12-19 13:57:53.323
                       资源ID   =  64   
    配置为节能模式时的容忍时长  =  0
配置为节能模式时的强制休眠阈值  =  0
配置为节能模式时的强制休眠时间  =  0
                      节能模式  =  H1
            性能参数收发包个数  =  128
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示FEI健康状态（DSP-FEIHEALTHSTATE）_00600829.md`
