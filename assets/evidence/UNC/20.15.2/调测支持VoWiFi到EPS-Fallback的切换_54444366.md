# 调测支持VoWiFi到EPS Fallback的切换

- [操作场景](#ZH-CN_OPI_0000002054444366__1.3.1)
- [必备事项](#ZH-CN_OPI_0000002054444366__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000002054444366__1.3.3)

## [操作场景](#ZH-CN_OPI_0000002054444366)

当已要部署VoWiFi到VoNR切换支持EPS Fallback功能时，需要对本功能进行调测，确保本功能可以正常使用。

## [必备事项](#ZH-CN_OPI_0000002054444366)

前提条件

- 请仔细阅读[WSFD-201305 支持VoWiFi到EPS Fallback的切换特性概述](WSFD-201305 支持VoWiFi到EPS Fallback的切换特性概述_90523317.md)。
- 完成[激活支持VoWiFi到EPS Fallback的切换](激活支持VoWiFi到EPS Fallback的切换_90444765.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息 | 国际移动用户识别码（IMSI） | 123000123456789 | 测试终端自带 | - |

## [操作步骤](#ZH-CN_OPI_0000002054444366)

1. 终端在WiFi上已存在默认承载和语音专有专载，从VoWifi切换到VoNR。
2. SMF通过AMF通知基站创建会话资源，基站回复消息，AMF向SMF发送Nsmf_PDUSession_UpdateSmContext Request（N2SmInfoTypePDU_RES_SETUP_FAIL），通知SMF语音QoS Flow资源创建失败。
  ```
  ------HTTP-TRACE-BEGIN------
  domain: request, role: server
  local_addr:10.2.126.13:33178  peer_addr:10.70.78.1:5054  protocol: TCP  msgtype:117571593
  rid=344542376, scheme=https, stream id=21
  POST /nsmf-pdusession/v1/sm-contexts/2147811339/modify HTTP/2.0
  host: 10.2.126.13:33178
  content-type: multipart/related; boundary=----Boundary
  content-type: application/json
  date: Tue, 05 Nov 2024 08:30:34 GMT
  bodytype: multipart
  content-length: 509
  user-agent: Go-http-client/2.0
  ------Boundary
  Content-Type: application/json
  {
  	"servingNetwork":{
  		"mnc":"00",
  		"mcc":"123"
  	},
  	"n2SmInfo":{
  		"contentId":"n2smInfo"
  	},
  	"anType":"3GPP_ACCESS",
  	"guami":{
  		"plmnId":{
  			"mnc":"00",
  			"mcc":"123"
  		},
  		"amfId":"000042"
  	},
	
  "n2SmInfoType":"PDU_RES_SETUP_FAIL"
  ,
          ...
  }
  ------Boundary
  Content-Id: n2smInfo
  Content-Type: application/vnd.3gpp.ngap
                         Ngap-Msg
    message:01 20 
  ------Boundary--
  ------HTTP-TRACE-END------
  ```
3. SMF在定时器超时内收到SGW/MME的Create Session Request消息，指示当前会话切换到EPC，发起5到4的切换。
  ![](调测支持VoWiFi到EPS Fallback的切换_54444366.assets/zh-cn_image_0000002076791504_2.png "点击放大")
