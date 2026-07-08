# 删除重定向携带信息（RMV REDIRAPPENDINFO）

- [命令功能](#ZH-CN_CONCEPT_0186528788__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186528788__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186528788__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186528788__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186528788__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0186528788)

**适用NF：PGW-U、UPF**

此命令用于运营商删除已经配置的重定向携带信息。

#### [注意事项](#ZH-CN_CONCEPT_0186528788)

- 该命令执行后立即生效。
- 输入APPENDINFONAME删除指定记录，不输入APPENDINFONAME删除所有记录。
- 如果被Redirect、FuiEnrichment、GyOneshot、SmartHttpRedir、IPFarmServer引用则不允许删除，需先解除绑定，才能删除。

#### [操作用户权限](#ZH-CN_CONCEPT_0186528788)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186528788)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPENDINFONAME | 重定向携带信息名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置重定向携带信息名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186528788)

运营商希望删除名为“testredirappendinfo”的重定向携带信息：

```
RMV REDIRAPPENDINFO: APPENDINFONAME="testredirappendinfo";
```
