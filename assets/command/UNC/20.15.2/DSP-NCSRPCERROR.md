---
id: UNC@20.15.2@MMLCommand@DSP NCSRPCERROR
type: MMLCommand
name: DSP NCSRPCERROR（显示最近的RPC和错误RPC响应报文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCSRPCERROR
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议
status: active
---

# DSP NCSRPCERROR（显示最近的RPC和错误RPC响应报文信息）

## 功能

该命令用于显示最近的解析正常但执行错误的RPC和RPC响应报文信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BOARDTYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- master：主OMU。<br>- slave：备OMU。<br>默认值：master |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCSRPCERROR]] · 最近的RPC和错误RPC响应报文信息（NCSRPCERROR）

## 使用实例

显示最近的解析正常但执行错误的RPC和RPC响应报文信息：

```
DSP NCSRPCERROR:BOARDTYPE=master
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
---------
通道ID  会话ID  时间戳                     用户名        终端地址         RPC报文        RPC响应报文

134754  625     2024-02-29 17:51:27+08:00  internaluser  192.168.0.1  <?xml version="1.0" encoding="GBK"?>
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="249638">
  <edit-config>
    <target>
      <running/>
    </target>
    <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <DIAM_PROTO_MGMT xmlns="urn:Huawei:yang:huawei-DIAM_PROTO_MGMT">
        <DOMDMPEERs>
          <DOMDMPEER xc:operation="create">
            <FCOUTSWT>CLOSE</FCOUTSWT>
            <BINDINGFLAG>NO</BINDINGFLAG>
            <SPM>2097152</SPM>
            <DIAMPEERPPNAME>Default</DIAMPEERPPNAME>
            <DN>A</DN>
            <TIMEOUTPLC>DISCARD</TIMEOUTPLC>
            <PEERTIMER>0</PEERTIMER>
            <DIRPROXY>CLOSE</DIRPROXY>
            <DEVTPCHKINSWT>CLOSE</DEVTPCHKINSWT>
            <DEVTPCHKOUTSWT>CLOSE</DEVTPCHKOUTSWT>
            <OAPNAP>NO</OAPNAP>
            <IAPNAP>NO</IAPNAP>
            <DEVTP>1</DEVTP>
            <SLFFLAG>Not_query_the_SLF</SLFFLAG>
            <BWSWT>OFF</BWSWT>
            <INMDENTNM>A</INMDENTNM>
            <HN>A</HN>
            <RN>A</RN>
            <LKSSMOD>ROUND_ROBIN</LKSSMOD>
            <TOPHIDETAG>No</TOPHIDETAG>
            <FCINSWT>CLOSE</FCINSWT>
          </DOMDMPEER>
        </DOMDMPEERs>
      </DIAM_PROTO_MGMT>
    </config>
  </edit-config>
</rpc>
     <?xml version="1.0" encoding="GBK"?>
<rpc-reply message-id="249638" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" flow-id="64">
  <rpc-error>
    <error-type>application</error-type>
    <error-tag>operation-failed</error-tag>
    <error-severity>error</error-severity>
    <error-app-tag>4790</error-app-tag>
    <error-message xml:lang="ch">操作异常。</error-message>
    <error-info xmlns:nc-ext="urn:huawei:yang:huawei-ietf-netconf-ext">
      <nc-ext:error-info-code>4790</nc-ext:error-info-code>
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NCSRPCERROR.md`
