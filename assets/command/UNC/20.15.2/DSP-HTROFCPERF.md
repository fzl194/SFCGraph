---
id: UNC@20.15.2@MMLCommand@DSP HTROFCPERF
type: MMLCommand
name: DSP HTROFCPERF（显示HTR局向统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: HTROFCPERF
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
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- HTR流控局向管理
- 流控局向查询
- 查询HTR局向统计信息
status: active
---

# DSP HTROFCPERF（显示HTR局向统计信息）

## 功能

**适用网元：SGSN、MME**

该命令用于查询HTR局向的流控统计信息。

## 注意事项

当执行此命令时，最多输出系统缓存的100个周期的数据，每个周期时长为20秒。命令的输出结果分为两部分，第一部分为最多9条“局向周期数据”；第二部分为最多91条“历史流控数据”。每个20秒统计周期结束时，系统会将上周期的数据刷新保存在“局向周期数据”中；如果上周期的数据是流控状态的，也会同时刷新保存在“历史流控数据”中。命令的显示结果会去除“局向周期数据”和“历史流控数据”中的重复数据。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [HTR局向统计信息（HTROFCPERF）](configobject/UNC/20.15.2/HTROFCPERF.md)

## 使用实例

查询HTR局向统计信息命令如下：

DSP HTROFCPERF:;

```
%%DSP HTROFCPERF:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
 局向索引     局向名称     统计周期序号     周期开始时间              发出请求数    接收应答数    被流控的请求数     周期WAL  周期成功率  流程平均时延
 0            Unified HTR  1335             2014-12-26 02:31:29       16002         15996         0                  19257    99          410    
 0            Unified HTR  1336             2014-12-26 02:31:49       16001         16004         0                  19257    100         410    
 0            Unified HTR  1337             2014-12-26 02:32:09       16006         16004         0                  19257    99          410    
 0            Unified HTR  1338             2014-12-26 02:32:29       15992         15991         0                  19257    99          409    
 0            Unified HTR  1339             2014-12-26 02:32:49       16006         16012         0                  18294    100         409    
 (结果个数 = 5)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示HTR局向统计信息(DSP-HTROFCPERF)_26146148.md`
