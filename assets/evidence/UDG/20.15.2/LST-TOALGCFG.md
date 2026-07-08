# 查询TCP算法配置（LST TOALGCFG）

- [命令功能](#ZH-CN_CONCEPT_0000201344249106__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201344249106__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201344249106__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201344249106__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201344249106__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000201344249106__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201344249106)

**适用NF：UPF**

该命令用于查询TCP算法配置。

#### [注意事项](#ZH-CN_CONCEPT_0000201344249106)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201344249106)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201344249106)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000201344249106)

查询TCP算法配置：

```
LST TOALGCFG:;
```

```

RETCODE = 0  操作成功

TCP算法配置
-----------
TCP拥塞控制算法  =  CCALG_CUBIC
慢启动阶段的门限值计算因子  =  717
启动hybrid slow start算法  =  ENABLE
初始拥塞窗口  =  64
TCP初始接收窗口  =  64
启动hybrid slow start算法的最小拥塞窗口门限值  =  512
Forward Acknowledgement算法  =  ENABLE
每个套接字TCP队列的大小  =  131072
(结果个数 = 1)

--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000201344249106)

参见SET TOALGCFG的参数说明。
