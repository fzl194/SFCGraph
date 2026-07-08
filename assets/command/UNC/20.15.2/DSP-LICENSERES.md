---
id: UNC@20.15.2@MMLCommand@DSP LICENSERES
type: MMLCommand
name: DSP LICENSERES（显示License资源）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LICENSERES
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# DSP LICENSERES（显示License资源）

## 功能

该命令用于显示License资源的使用状况。该命令执行后，返回业务模块总的License资源使用状况。

## 注意事项

- QBM进程的单点故障会对资源结果进行清空，造成结果不准确，因此查询时应保证QBM进程的状态正常，并且稳定运行半小时以上。
- 当资源数超过License限制后，后续新增资源将不统计。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/LICENSERES]] · License资源（LICENSERES）

## 使用实例

显示License资源使用状况：

```
DSP LICENSERES:;
```

```
RETCODE = 0  操作成功。

结果如下:
---------
资源项         资源名称                              资源总数    已使用资源    使用率

LKV7RIPV601    支持用户面IPv6 PDP（每千PDP/承载）    12000       0             0%    
LKV7CDRS01     每秒话单数（CDR/秒）                  32000       0             0%    
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示License资源（DSP-LICENSERES）_51174310.md`
