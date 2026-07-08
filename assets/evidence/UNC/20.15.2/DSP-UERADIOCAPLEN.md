# 显示UE Radio Capability信元长度（DSP UERADIOCAPLEN）

- [命令功能](#ZH-CN_MMLREF_0000001171436533__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001171436533__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001171436533__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001171436533__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001171436533__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001171436533)

**适用NF：AMF**

该命令用于显示AMF存储的UE Radio Capability信元长度信息。

## [注意事项](#ZH-CN_MMLREF_0000001171436533)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001171436533)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001171436533)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODID | POD ID | 可选必选说明：必选参数<br>参数含义：该参数用于标识系统中的POD ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001171436533)

查询PODID为uncpod-0的UE Radio Capability信元长度，执行如下命令：

```
%%DSP UERADIOCAPLEN: PODID="uncpod-0";%%
RETCODE = 0  操作成功

结果如下
--------
                         POD ID  =  uncpod-0
           IMEI设备型号核准号码  =  35437906
UE Radio Capability信元最小长度  =  1024
UE Radio Capability信元最大长度  =  4096
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001171436533)

| 输出项名称 | 输出项解释 |
| --- | --- |
| POD ID | 该参数用于标识系统中的POD ID。 |
| IMEI设备型号核准号码 | 该参数用于指定用户的设备型号核准号码（TAC）。TAC由IMEI的前8位数字组成，用来标识某一型号的手机。 |
| UE Radio Capability信元最小长度 | 该参数用于标识系统中某个TAC下的UE Radio Capability信元的最小长度。 |
| UE Radio Capability信元最大长度 | 该参数用于标识系统中某个TAC下的UE Radio Capability信元的最大长度。 |
