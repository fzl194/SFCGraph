---
id: UNC@20.15.2@MMLCommand@LST ADDRPARA
type: MMLCommand
name: LST ADDRPARA（查询ADDR参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ADDRPARA
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- ADDR地址分配参数配置
status: active
---

# LST ADDRPARA（查询ADDR参数）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询ADDR参数，包括核查速率、去活间隔等参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ADDRPARA]] · ADDR参数（ADDRPARA）

## 使用实例

该命令用于查询ADDRPARA配置： LST ADDRPARA:;

```
%%LST ADDRPARA:;%%
RETCODE = 0  操作成功

结果如下
--------------------
同步地址使用情况数据时间间隔(秒)  =  300
        转发地址申请最大次数(次)  =  2
     地址使用情况核查速率(个/秒)  =  2
 地址子段分配情况核查速率(个/秒)  =  2
             租约核查速率(个/秒)  =  2
             地址回收速率(个/秒)  =  6
            地址使用情况核查开关  =  是
        地址子段分配情况核查开关  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ADDRPARA.md`
