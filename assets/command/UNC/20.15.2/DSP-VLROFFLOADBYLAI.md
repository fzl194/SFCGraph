---
id: UNC@20.15.2@MMLCommand@DSP VLROFFLOADBYLAI
type: MMLCommand
name: DSP VLROFFLOADBYLAI（显示IMSI分离4G用户任务运行状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: VLROFFLOADBYLAI
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- MSC POOL管理
- 基于LAI的IMSI分离业务
status: active
---

# DSP VLROFFLOADBYLAI（显示IMSI分离4G用户任务运行状态）

## 功能

**适用网元：MME**

用户通过 [**STR VLROFFLOADBYLAI**](启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.md) 启动对4G用户的IMSI分离任务后，执行本命令可以查询该任务的运行状态等信息。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [IMSI分离4G用户任务（VLROFFLOADBYLAI）](configobject/UNC/20.15.2/VLROFFLOADBYLAI.md)

## 使用实例

查询 [**STR VLROFFLOADBYLAI**](启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.md) 启动的IMSI分离4G用户扫描任务的运行状态和进度：

DSP VLROFFLOADBYLAI:;

```
%%DSP VLROFFLOADBYLAI:;%%
RETCODE = 0  操作成功。

操作结果如下：
--------------
               任务的运行状态  =  正在运行
            任务的处理进度(%)  =  60
                 已处理用户数  =  16000
已发起IMSI Detach请求的用户数  =  8000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示IMSI分离4G用户任务运行状态(DSP-VLROFFLOADBYLAI)_26145426.md`
