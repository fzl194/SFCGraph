---
id: UDG@20.15.2@MMLCommand@LST VNFC
type: MMLCommand
name: LST VNFC（查询VNFC）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VNFC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 配置管理
- VNFC信息
status: active
---

# LST VNFC（查询VNFC）

## 功能

该命令用于查询VNFC实例。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNFCNAME | VNFC名称 | 可选必选说明：可选参数<br>参数含义：VNFC名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [重启系统（VNFC）](configobject/UDG/20.15.2/VNFC.md)

## 使用实例

查询VNFC：

```
LST VNFC:;
```

```
 
RETCODE = 0  操作成功

结果如下:
-------------------------
VNFC名称    VNFC类型名称     资源类型    VM1的名称    VM2的名称    基础版本           补丁版本          初始启动配置文件名称   管理代理标识    初始启动主密钥文件的名称

VNFP        VNFP             无          NULL         NULL         V100R018C00B110    NULL              NULL                   0               NULL               
kk          VNRS_VNFC        无          NULL         NULL         V100R018C00B110    NULL              NULL                   ll              NULL               
yy          CSDB_VNFC        无          NULL         NULL         V100R018C00B110    NULL              NULL                   yy              NULL               
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询VNFC（LST-VNFC）_59036046.md`
