# 查询Diameter域路由优先级权重(LST DMRTPRI)

- [命令功能](#ZH-CN_MMLREF_0000001126146288__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126146288__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126146288__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126146288__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126146288__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126146288__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126146288__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126146288)

**适用网元：SGSN、MME**

该命令用于查询Diameter域路由优先级和权重。

#### [注意事项](#ZH-CN_MMLREF_0000001126146288)

该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126146288)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126146288)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126146288)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROUTEIDX | 路由索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定准备查询的Diameter域路由索引。<br>取值范围：0～2047<br>默认值：无 |
| PEERIDX | 对端实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端索引，用于标识目的对端。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD DMPE**](../Diameter对端实体/增加Diameter对端实体(ADD DMPE)_72225963.md)<br>设置此参数。<br>取值范围：0～639<br>默认值：无<br>说明：一个域路由下最多配置16个对端。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定域路由中对端的优先级。<br>前提条件：该参数只在<br>[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)<br>命令中的<br>“选路模式”<br>设置为<br>“SELMODE_MASTER_SLAVE(主从)”<br>、<br>“SELMODE_PRIORITY_WEIGHT(优先级权重)”<br>或者<br>“SELMODE_IMSI_PRIORITY(IMSI指定优选)”<br>时有效。<br>取值范围：0~255<br>默认值：无<br>说明：- “SELMODE_MASTER_SLAVE(主从)”模式下，同一个域路由中不同对端的优先级不允许相同。<br>- 数值越小，优先级越高。 |
| WEIGHT | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定域路由中对端的权重。<br>前提条件：该参数只在<br>[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)<br>命令中的<br>“选路模式”<br>设置为<br>“SELMODE_PRIORITY_WEIGHT(优先级权重)”<br>时有效。<br>取值范围：1~255<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126146288)

查询所有记录的优先级：

LST DMRTPRI:;

```
%%LST DMRTPRI:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
 路由索引  对端实体索引     优先级    权重

 0          0               0     NULL
 1          1               1     NULL
(结果个数 = 2)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126146288)

请参考 [**MOD DMRTPRI**](修改Diameter域路由优先级权重(MOD DMRTPRI)_72345887.md) 命令的参数标识。
