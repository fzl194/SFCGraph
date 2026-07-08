---
id: UNC@20.15.2@MMLCommand@LST GBSM
type: MMLCommand
name: LST GBSM（查询Gb模式SM协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBSM
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- SM协议参数管理
- Gb模式SM协议参数
status: active
---

# LST GBSM（查询Gb模式SM协议参数）

## 功能

**适用网元：SGSN**

该命令用于查看GBSM协议配置信息，包括QoS参数、定时器参数、流程执行控制标志等。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBSM]] · Gb模式SM协议参数（GBSM）

## 使用实例

查询GBSM协议配置信息：

LST GBSM:;

```
%%LST GBSM:;%%
RETCODE = 0  操作成功。

2G SM协议配置表
---------------
                        T3385(s)  =  8
                    N3385(times)  =  4
                        T3386(s)  =  8
                    N3386(times)  =  4
                        T3395(s)  =  8
                    N3395(times)  =  4
                     是否启用PFT  =  Yes
       BSS保留PFC的时长定时器(s)  =  40
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Gb模式SM协议参数(LST-GBSM)_26145702.md`
