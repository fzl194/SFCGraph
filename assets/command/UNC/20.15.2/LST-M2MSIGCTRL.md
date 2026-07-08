---
id: UNC@20.15.2@MMLCommand@LST M2MSIGCTRL
type: MMLCommand
name: LST M2MSIGCTRL（查询M2M信令控制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: M2MSIGCTRL
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- M2M信令控制
status: active
---

# LST M2MSIGCTRL（查询M2M信令控制配置）

## 功能

**适用网元：MME**

该命令用于查询M2M用户的信令控制。

## 注意事项

通信次数参数值为65535时，LST执行结果显示为NULL

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFGINDEX | 配置索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信令控制策略的索引。<br>数据来源：本端规划<br>取值范围：0～31<br>默认值：无 |

## 操作的配置对象

- [M2M信令控制配置（M2MSIGCTRL）](configobject/UNC/20.15.2/M2MSIGCTRL.md)

## 使用实例

查询M2M信令控制配置：

LST M2MSIGCTRL:;

```
%%LST M2MSIGCTRL:;%%
RETCODE = 0  操作成功

操作结果如下
--------------
            配置索引  =  1
    业务受限控制开关  =  关闭
    通信包数控制开关  =  关闭
         SMS控制开关  =  关闭
            通信包数  =  NULL
通信持续时长控制开关  =  关闭
    通信持续时长(秒)  =  NULL
    通信周期控制开关  =  关闭
    通信周期时间单位  =  分钟
            通信周期  =  NULL
  每周期允许通信次数  =  NULL
    通信时段控制开关  =  关闭
            通信频度  =  日
              星期几  =  NULL
                日期  =  NULL
            起始时间  =  00:00:00
            终止时间  =  00:00:00
            通信次数  =  NULL
                描述  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询M2M信令控制配置(LST-M2MSIGCTRL)_72225447.md`
