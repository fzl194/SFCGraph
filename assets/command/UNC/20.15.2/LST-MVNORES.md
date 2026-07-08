---
id: UNC@20.15.2@MMLCommand@LST MVNORES
type: MMLCommand
name: LST MVNORES（查询MVNO资源配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MVNORES
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- MVNO管理
- MVNO资源配置表
status: active
---

# LST MVNORES（查询MVNO资源配置信息）

## 功能

**适用网元：SGSN、MME**

查询MVNO的用户资源信息。MVNO的用户资源配置了这个MVNO可以附着和激活的最大的用户数。MVNO的用户资源有：2G最大附着用户数、3G最大附着用户数、4G最大附着用户数、2G最大PDP激活数、3G最大PDP激活数、4G最大激活承载数。如果配置了一个MVNO，但是不给这个MVNO配置用户资源，MVNO的用户不能进行PS业务。

## 注意事项

如果不输入参数，查询所有的MVNO的资源信息。如果输入参数，则查询指定的MVNO的资源信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MVNOID | MVNO标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要查询的MVNO的标识。<br>取值范围：1～64<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MVNORES]] · MVNO资源配置信息（MVNORES）

## 使用实例

查询所有的MVNO的用户资源：

LST MVNORES:;

```
%%LST MVNORES:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
              MVNO标识  =  2
              2G用户数  =  50000
        2G用户拥塞门限  =  85
    2G用户拥塞恢复门限  =  75
              3G用户数  =  50000
        3G用户拥塞门限  =  85
    3G用户拥塞恢复门限  =  75
              4G用户数  =  50000
        4G用户拥塞门限  =  85
    4G用户拥塞恢复门限  =  75
           2G激活PDP数  =  50000
     2G激活PDP拥塞门限  =  85
 2G激活PDP拥塞恢复门限  =  75
           3G激活PDP数  =  50000
     3G激活PDP拥塞门限  =  85
 3G激活PDP拥塞恢复门限  =  75
          4G建立承载数  =  50000
    4G建立承载拥塞门限  =  85
4G建立承载拥塞恢复门限  =  75
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MVNO资源配置信息(LST-MVNORES)_26305876.md`
