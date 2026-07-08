# 查询NRF密钥（LST SBINRFKEY）

- [命令功能](#ZH-CN_MMLREF_0000001229053333__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001229053333__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001229053333__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001229053333__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001229053333__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001229053333)

该命令用于查询NF认证所需的公钥信息。5G核心网NF间基于OAuth2.0框架使用token进行认证，NRF通过私钥对token进行数字签名，NF服务提供者通过对应的公钥校验token的数字签名是否合法。

## [注意事项](#ZH-CN_MMLREF_0000001229053333)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001229053333)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001229053333)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFID | NRF实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置的NRF实例ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001229053333)

若运营商想查询配置的NRF密钥信息，可以用如下命令：

```
%%LST SBINRFKEY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
      NRF实例ID  =  bf33a517-7789-4637-b675-b3591b0d706b
        NRF密钥  =  -----BEGIN PUBLIC KEY----- MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQA/axE26pXWXesAjcTP/2Tfe4EcF4A3LuqgpIFzrftiztViq0+5deUvfcxuPIFk+ANVinlAOzgZWpFS0kheI7KJAYA3fOHn5ZTU08AAjau0CoZe9GSPUC4cnSy1nqetiKBW0YpBvhaY5FXnngvfHUHdmkFSVLC S6N+LXoi/dm0Fbo6snE= -----END PUBLIC KEY-----
        密钥名称 =  key1
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001229053333)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NRF实例ID | 该参数用于指定配置的NRF实例ID。 |
| NRF密钥 | 该参数用于指定配置的NRF密钥。 |
| 密钥名称 | 该参数用于指定配置的密钥名称。 |
