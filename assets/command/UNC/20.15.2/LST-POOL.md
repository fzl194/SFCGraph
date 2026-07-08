---
id: UNC@20.15.2@MMLCommand@LST POOL
type: MMLCommand
name: LST POOL（查询POOL配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: POOL
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- POOL区配置
status: active
---

# LST POOL（查询POOL配置信息）

## 功能

**适用网元：SGSN**

该命令用于查询POOL配置信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示POOL标识。<br>取值范围：0~4095<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@POOL]] · POOL配置信息（POOL）

## 使用实例

查询POOL配置信息：

LST POOL:;

```
%%LST POOL:;%%
RETCODE = 0  执行成功。

查询POOL配置信息
-------------------------
 POOL标识  =  0
  NRI长度  =  2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-POOL.md`
