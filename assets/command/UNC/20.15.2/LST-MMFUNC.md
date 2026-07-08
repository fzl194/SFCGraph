---
id: UNC@20.15.2@MMLCommand@LST MMFUNC
type: MMLCommand
name: LST MMFUNC（查询移动性管理扩展功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MMFUNC
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MM扩展功能管理
status: active
---

# LST MMFUNC（查询移动性管理扩展功能）

## 功能

**适用网元：SGSN、MME**

此命令用于查询移动性管理扩展功能。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMFUNC]] · 移动性管理扩展功能（MMFUNC）

## 使用实例

查询移动性管理扩展功能：

LST MMFUNC:;

```
%%LST MMFUNC:;%%
RETCODE = 0  操作成功。

输出结果如下
------------
                是否支持QCI寻呼策略  =  是
                           保留参数  =  是
                   是否支持紧急号码  =  支持
                             区域码  =  是
                   区域关闭加密功能  =  启用
                       发送网络信息  =  Iu模式 & Gb模式 & S1模式
                     PS网络信息优先  =  S1模式
            EMM Information发送策略  =  MME间TAU & USN间异系统类型TAU & MME内TAU & USN内异系统类型TAU & 周期性TAU & MME间切换后的TAU & USN间异系统切换后的TAU & MME内切换后的TAU & USN内异系统切换后的TAU
  EMM Information消息的信元携带策略  =  NULL
               实时位置上报最小间隔  =  2
                         最近访问TA  =  YES
                        TA List过滤  =  NULL
                      Forbidden TAs  =  本地配置
         基于无线区域的网络地址选择  =  NULL
            允许跨共享运营商RAU/TAU  =  允许
    是否支持连接态向RNC发送签约SPID  =  支持
               是否支持语音优先寻呼  =  支持
S13接口增强的Check IMEI消息发送策略  =  NULL
     是否支持对20bit长HeNB的TAI寻址  =  是
     是否允许有VoLTE业务时切换到5GC  =  是
            是否刷新eNodeB上报的ULI  =  否
  是否开启S6a接口原因值映射优化开关  =  否
     是否允许
Network policy携带策略
  =  NO
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询移动性管理扩展功能(LST-MMFUNC)_72225193.md`
