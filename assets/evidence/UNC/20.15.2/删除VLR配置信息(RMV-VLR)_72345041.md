# 删除VLR配置信息(RMV VLR)

- [命令功能](#ZH-CN_MMLREF_0000001172345041__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345041__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345041__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345041__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345041__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345041__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345041)

**适用网元：SGSN、MME**

该命令用于删除一个与本局 UNC 相连的VLR的信息。

#### [注意事项](#ZH-CN_MMLREF_0000001172345041)

- 该命令执行后立即生效。
- 如果LAIVLR表[**ADD LAIVLR**](../LAI与VLR号对应关系/增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md)或SGSLNK表[**ADD SGSLNK**](../SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md)中有此VLR相关数据，则不能删除此VLR的信息。
- 如果没有增加VLR信息，也不能在RAIVLR表、SGSLNK表和NRA中增加此VLR的相关信息。
- 当MSC POOL中有VLR处于迁移状态时，不允许删除此MSC POOL中的VLR配置。
- 如果删除的VLR属于MSC POOL，建议把此VLR对应的V值重新分配到此MSC POOL中其他的VLR上以便此MSC POOL中的VLR能覆盖0～999所有的V值。
- 若该VLR属于某一个MSC POOL，执行该命令会把该VLR从MSC POOL中删除。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345041)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345041)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345041)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VN | VLR号 | 可选必选说明：必选参数<br>参数说明：该参数用于指定待删除的VLR号。<br>数据来源：整网规划<br>取值范围： 1～15位十进制数字<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345041)

删除VLR信息，VLR号为86139027：

```
RMV VLR: VN="86139027";
```
