---
id: UNC@20.15.2@MMLCommand@LST S1SMARTPARA
type: MMLCommand
name: LST S1SMARTPARA（查询S1模式信令抑制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1SMARTPARA
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- 异常信令节省
- S1模式信令抑制参数管理
status: active
---

# LST S1SMARTPARA（查询S1模式信令抑制参数）

## 功能

**适用网元：MME**

该命令用于查询S1模式异常信令抑制相关参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1SMARTPARA]] · S1模式信令抑制参数（S1SMARTPARA）

## 使用实例

查询S1模式异常信令抑制参数：

LST S1SMARTPARA:;

```
%%LST S1SMARTPARA:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
          附着异常识别门限（次）  =  30
          附着异常测量周期（秒）  =  3600
        附着异常抑制时长（分钟）  =  60
      服务请求异常识别门限（次）  =  100
      服务请求异常测量周期（秒）  =  3600
    服务请求异常抑制时长（分钟）  =  60
 控制面服务请求异常识别门限(次)   =  100
 控制面服务请求异常测量周期(秒)   =  3600
控制面服务请求异常抑制时长(分钟)  =  60
       PDN连接异常识别门限（次）  =  30
       PDN连接异常测量周期（秒）  =  3600
     PDN连接异常抑制时长（分钟）  =  60
                     Parking APN  =  PARKINGAPN
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-S1SMARTPARA.md`
