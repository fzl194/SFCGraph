---
id: UNC@20.15.2@MMLCommand@LST DDNTHROTPARA
type: MMLCommand
name: LST DDNTHROTPARA（查询DDN信令抑制参数）
nf: UNC
version: 20.15.2
verb: LST
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

# LST DDNTHROTPARA（查询DDN信令抑制参数）

## 功能

**适用网元：MME**

该命令用于查询DDN（Downlink Data Notification）信令抑制参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DDNTHROTPARA]] · DDN信令抑制状态（DDNTHROTPARA）

## 使用实例

1. 查询DDN信令抑制参数:LST DDNTHROTPARA:;
  ```
  %%LST DDNTHROTPARA:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
    DDN信令抑制功能开关  =  关闭
          启动门限（%）  =  80
  DDN信令抑制时长（秒）  =  60
     策略发送时长（秒）  =  2
  (结果个数 = 1)

  ---    END
  ```
2. 查询DDN信令抑制参数:LST DDNTHROTPARA:;
  ```
  %%LST DDNTHROTPARA:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
    DDN信令抑制功能开关  =  开启
          启动门限（%）  =  80
  DDN信令抑制时长（秒）  =  60
     策略发送时长（秒）  =  2
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DDNTHROTPARA.md`
