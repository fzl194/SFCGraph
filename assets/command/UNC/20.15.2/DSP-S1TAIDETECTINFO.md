---
id: UNC@20.15.2@MMLCommand@DSP S1TAIDETECTINFO
type: MMLCommand
name: DSP S1TAIDETECTINFO（显示S1 TAI对象寻呼流控状态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: S1TAIDETECTINFO
command_category: 查询类
applicable_nf:
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
- S1寻呼流控管理
- TA LIST流控
status: active
---

# DSP S1TAIDETECTINFO（显示S1 TAI对象寻呼流控状态信息）

## 功能

**适用网元：MME**

该命令用于查询S1 TAI对象寻呼流控状态信息。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@S1TAIDETECTINFO]] · S1 TAI对象寻呼流控状态信息（S1TAIDETECTINFO）

## 使用实例

查询系统中的所有S1 TAI对象寻呼流控状态，执行如下命令：

```
%%DSP S1TAIDETECTINFO:;%%
RETCODE = 0  操作成功。

输出结果如下
-----------------------
            任务ID =  monitor_task_5 
     检测任务状态  =  正常
    TAI组对象数量  =  0 
异常TAI组对象数量  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-S1TAIDETECTINFO.md`
