---
id: UNC@20.15.2@MMLCommand@LST IULOAD
type: MMLCommand
name: LST IULOAD（查询SGP负荷配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IULOAD
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Iu接口管理
- Iu负荷配置
status: active
---

# LST IULOAD（查询SGP负荷配置）

## 功能

**适用网元：SGSN**

该命令用于查询Iu接口负荷在SGP进程间分担的控制参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/IULOAD]] · 用户Iu连接负荷状态（IULOAD）

## 使用实例

查询IU接口负荷参数：

LST IULOAD:;

```
%%LST IULOAD:;%%
RETCODE = 0  操作成功。

IU负荷配置表
------------
           是否支持Iu负荷分担  =  是
    周期性通知定时器长度(min)  =  5
发送OVERLOAD消息定时器长度(s)  =  40
(结果个数 = 1)

---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGP负荷配置(LST-IULOAD)_72345637.md`
