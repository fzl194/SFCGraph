---
id: UNC@20.15.2@MMLCommand@LST UERADIOCAPLEN
type: MMLCommand
name: LST UERADIOCAPLEN（查询UE Radio Capability信元配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UERADIOCAPLEN
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- UE无线能力控制策略
status: active
---

# LST UERADIOCAPLEN（查询UE Radio Capability信元配置）

## 功能

**适用NF：AMF**

该命令用于查询AMF上存储UE Radio Capability到数据库的信元长度上限和不同IMEI设备型号核准号码的最大个数，查询存储UE Radio Capability到内存的开关及参数信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/UERADIOCAPLEN]] · UE Radio Capability信元长度（UERADIOCAPLEN）

## 使用实例

查询AMF上能存储的UE Radio Capability信元长度上限和不同IMEI设备型号核准号码的最大个数，执行如下命令：

```
%%LST UERADIOCAPLEN:;%%
RETCODE = 0  操作成功

结果如下
--------
   UE Radio Capability信元长度上限  =  4096
不同IMEI设备型号核准号码的最大个数  =  1024
                    保存到内存开关  =  ON
          保存到内存的用户数百分比  =  20
                      最大长度(KB)  =  32
                      内存配额(MB)  =  200
                    上报告警百分比  =  95
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UE-Radio-Capability信元配置（LST-UERADIOCAPLEN）_71436545.md`
