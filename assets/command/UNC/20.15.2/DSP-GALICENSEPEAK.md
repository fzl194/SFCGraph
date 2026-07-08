---
id: UNC@20.15.2@MMLCommand@DSP GALICENSEPEAK
type: MMLCommand
name: DSP GALICENSEPEAK（显示GA接口话务高峰信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GALICENSEPEAK
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- GA接口License峰值
status: active
---

# DSP GALICENSEPEAK（显示GA接口话务高峰信息）

## 功能

**适用NF：NCG**

该命令用于显示GA接口话务高峰信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GALICENSEPEAK]] · GA接口话务高峰信息（GALICENSEPEAK）

## 使用实例

显示GA接口话务高峰信息，示例如下：

```
DSP GALICENSEPEAK:;
```

```
RETCODE = 0  操作成功  
已使用的峰值License记录 
-----------------------
      使用日期  =  2024-10-08 至 2024-10-10
 过载License项  =  4G Bearers数,5G Bearers数
(结果个数 = 1)  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GALICENSEPEAK.md`
