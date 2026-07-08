---
id: UNC@20.15.2@MMLCommand@LST SBINRFKEY
type: MMLCommand
name: LST SBINRFKEY（查询NRF密钥）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SBINRFKEY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP OAuth安全管理
status: active
---

# LST SBINRFKEY（查询NRF密钥）

## 功能

该命令用于查询NF认证所需的公钥信息。5G核心网NF间基于OAuth2.0框架使用token进行认证，NRF通过私钥对token进行数字签名，NF服务提供者通过对应的公钥校验token的数字签名是否合法。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFID | NRF实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置的NRF实例ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBINRFKEY]] · NRF密钥（SBINRFKEY）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF密钥（LST-SBINRFKEY）_29053333.md`
