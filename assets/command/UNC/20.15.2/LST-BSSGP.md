---
id: UNC@20.15.2@MMLCommand@LST BSSGP
type: MMLCommand
name: LST BSSGP（查询BSSGP参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BSSGP
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

# LST BSSGP（查询BSSGP参数）

## 功能

**适用网元：SGSN**

该命令用于查询BSSGP层系统参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BSSGP]] · BSSGP参数（BSSGP）

## 使用实例

查询BSSGP参数:

LST BSSGP:;

```
%%LST BSSGP:;%%
RETCODE = 0  操作成功。

操作结果如下
---------------
        保证Reset的时钟值(ms)  =  30000
             MS流控有效值(ms)  =  6000
          BVC复位消息重发次数  =  3
     BVC流控发送的最小间隔(s)  =  1
        创建PFC监控定时器(ms)  =  3000
          创建PFC消息重发次数  =  5
             流控缓存时间(ms)  =  12000
   PDU生存时间(centi-seconds)  =  700
                 小区拥塞门限  =  85
             小区拥塞恢复门限  =  75
闭塞小区的删除定时器时长(min)  =  0
        BSSID与NSEI的对应关系  =  NSEI
         是否关闭BSSGP小区流控 = 是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BSSGP.md`
