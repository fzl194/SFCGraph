---
id: UNC@20.15.2@MMLCommand@DSP OFFLOADAMF
type: MMLCommand
name: DSP OFFLOADAMF（显示AMF迁移任务）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OFFLOADAMF
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF Pool 迁移控制
status: active
---

# DSP OFFLOADAMF（显示AMF迁移任务）

## 功能

**适用NF：AMF**

该命令用于查询AMF用户迁移进度信息。

## 注意事项

- 如果当前系统正在执行迁移任务，则显示当前迁移进度信息，否则将显示最近一次的迁移记录信息。
- 此命令对类型为“IMSI(IMSI)”的迁移任务不生效。针对类型为“IMSI(IMSI)”的迁移任务，可通过用户跟踪等手段查看迁移进度。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [AMF迁移任务（OFFLOADAMF）](configobject/UNC/20.15.2/OFFLOADAMF.md)

## 使用实例

查询AMF用户迁移任务进度信息，执行如下命令：

```
%%DSP OFFLOADAMF:;%%
RETCODE = 0  操作成功

结果如下
------------------------
               迁移类型  =  全部用户
               迁移状态  =  迁移中
                目标AMF  =  NULL
         目标AMF IP信息  =  NULL
           迁移启动时间  =  2019-12-23 12:09:54 +0800
           待迁移用户数  =  1
           已迁移用户数  =  0
     迁移任务时长(分钟)  =  0
         剩余时间(分钟)  =  1
设定的迁移速率(千/分钟)  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示AMF迁移任务（DSP-OFFLOADAMF）_09653667.md`
