---
id: UNC@20.15.2@MMLCommand@DSP HTROFCINFO
type: MMLCommand
name: DSP HTROFCINFO（显示HTR局向信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: HTROFCINFO
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
- 查询HTR局向信息
status: active
---

# DSP HTROFCINFO（显示HTR局向信息）

## 功能

**适用网元：SGSN、MME**

用于查询HTR局向信息。

## 注意事项

- 由于[**SET UNIHTR**](../../统一HTR流控局向管理/统一HTR流控功能管理/设置统一HTR功能(SET UNIHTR)_26305954.md)中“初始启控速率（个/秒）”平分到各SPP进程后会有取整误差，所以实际初始启控速率和设置值可能不一样。
- 当局向状态为“流控状态”时，实际初始启控速率的值和ALM-10754 统一HTR流控启控告警中“初始起控速率（个/秒）”的值保持一致；当局向状态为“初始状态”时，实际初始启控速率的值为当前周期的WAL值/20秒。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [HTR局向信息（HTROFCINFO）](configobject/UNC/20.15.2/HTROFCINFO.md)

## 使用实例

查询HTR局向信息命令如下：

DSP HTROFCINFO:;

```
%%DSP HTROFCINFO:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
		    局向索引 = 0
		    局向名称 = Unified HTR
		    局向状态 = 流控状态
	初始启控速率（个/秒）= 2000 
	最大流控速率（个/秒）= 5000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示HTR局向信息(DSP-HTROFCINFO)_26305956.md`
