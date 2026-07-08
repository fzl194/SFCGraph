---
id: UNC@20.15.2@MMLCommand@LST SGSPARA
type: MMLCommand
name: LST SGSPARA（查询SGs参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGSPARA
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- SGSAP
- SGsAP参数管理
status: active
---

# LST SGSPARA（查询SGs参数）

## 功能

**适用网元：MME**

此命令用于查询SGs接口业务运行参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [SGs参数（SGSPARA）](configobject/UNC/20.15.2/SGSPARA.md)

## 使用实例

查询SGs接口业务运行参数：

LST SGSPARA:;

```
%%LST SGSPARA:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
              位置更新定时器(s)  =  10
               EPS分离定时器(s)  =  4
          显式IMSI分离定时器(s)  =  4
          隐式IMSI分离定时器(s)  =  4
       MME复位标志定时器增量(s)  =  8
MME复位指示MSC/VLR响应定时器(s)  =  4
         EPS分离重发次数(times)  =  2
    显式IMSI分离重发次数(times)  =  2
    隐式IMSI分离重发次数(times)  =  2
     MME复位指示重发次数(times)  =  2
     SGs链路中断触发告警阈值(s)  =  24
                   自动迁移开关  =  是
       连接态下CSFB被叫优化开关  =  是
      通知MSC前转取消的消息类型  =  SGsAP-UE-UNREACHABLE
              MSC Reset处理模式  =  标准模式
                MME复位指示功能  =  不启用
         VoLTE通话中拒绝SGs寻呼  =  否
     MSC Reset处理的VLR选择方式  =  VLR Number
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGs参数(LST-SGSPARA)_72225121.md`
