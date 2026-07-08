---
id: UNC@20.15.2@MMLCommand@LST FLOWCTRLBUF
type: MMLCommand
name: LST FLOWCTRLBUF（查询流量控制缓存配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FLOWCTRLBUF
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- BSSGP参数
status: active
---

# LST FLOWCTRLBUF（查询流量控制缓存配置）

## 功能

**适用网元：SGSN**

该命令用于查询BSSGP流控缓存参数配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/FLOWCTRLBUF]] · 流量控制缓存配置（FLOWCTRLBUF）

## 使用实例

查询BSSGP流控缓存配置：

LST FLOWCTRLBUF:;

```
%%LST FLOWCTRLBUF:;%%
RETCODE = 0  执行成功。

操作结果如下
------------------
  MS信令队列最大长度  =  32
  MS数据队列最大长度  =  512
       MS拥塞门限(%)  =  80
   MS拥塞恢复门限(%)  =  60
 BVC信令队列最大长度  =  256
 BVC数据队列最大长度  =  1024
      BVC拥塞门限(%)  =  80
  BVC拥塞恢复门限(%)  =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询流量控制缓存配置(LST-FLOWCTRLBUF)_26305798.md`
