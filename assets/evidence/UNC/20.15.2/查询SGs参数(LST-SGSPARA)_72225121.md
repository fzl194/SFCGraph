# 查询SGs参数(LST SGSPARA)

- [命令功能](#ZH-CN_MMLREF_0000001172225121__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225121__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225121__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225121__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225121__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225121__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172225121__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225121)

**适用网元：MME**

此命令用于查询SGs接口业务运行参数。

#### [注意事项](#ZH-CN_MMLREF_0000001172225121)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225121)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225121)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225121)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001172225121)

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

#### [输出结果说明](#ZH-CN_MMLREF_0000001172225121)

参见 [**SET SGSPARA**](设置SGs参数(SET SGSPARA)_26145440.md) 的参数说明。
