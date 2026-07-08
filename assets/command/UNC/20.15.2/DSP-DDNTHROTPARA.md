---
id: UNC@20.15.2@MMLCommand@DSP DDNTHROTPARA
type: MMLCommand
name: DSP DDNTHROTPARA（显示DDN信令抑制状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DDNTHROTPARA
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
- DDN信令抑制参数管理
status: active
---

# DSP DDNTHROTPARA（显示DDN信令抑制状态）

## 功能

**适用网元：MME**

该命令用于显示DDN（Downlink Data Notification）信令抑制状态。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [DDN信令抑制状态（DDNTHROTPARA）](configobject/UNC/20.15.2/DDNTHROTPARA.md)

## 使用实例

1. 显示DDN信令抑制状态。DSP DDNTHROTPARA:;
  ```
  %%DSP DDNTHROTPARA:;%%
  RETCODE = 0  操作成功。

  查询结果如下
  --------------
  抑制状态  =  未启动
  (结果个数 = 1)

  ---    END
  ```
2. 显示DDN信令抑制状态。DSP DDNTHROTPARA:;
  ```
  %%DSP DDNTHROTPARA:;%%
  RETCODE = 0  操作成功。

  查询结果如下
  --------------
       抑制状态  =  已启动
  抑制比例（%）  =  98
       抑制时长  =  3
   抑制时长单位  =  10分钟
  (结果个数 = 1)

  ---    END
  ```
3. 显示DDN信令抑制状态。DSP DDNTHROTPARA:;
  ```
  %%DSP DDNTHROTPARA:;%%
  RETCODE = 0  操作成功。

  查询结果如下
  --------------
       抑制状态  =  已启动
  抑制比例（%）  =  0
       抑制时长  =  3
   抑制时长单位  =  1小时
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示DDN信令抑制状态(DSP-DDNTHROTPARA)_26146172.md`
